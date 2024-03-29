import { Pool, PoolClient } from "postgres/mod.ts";
import { singleton } from "tsyringe";
import { ConfigProvider } from "@/services/config/ConfigProvider.ts";

export type DBClient = {
  queryObject: PoolClient["queryObject"];
  createTransaction: PoolClient["createTransaction"];
};

export type WithClientFunc = <T>(cb: (c: DBClient) => Promise<T>) => Promise<T>;

@singleton()
export class Database {
  private pool: Pool;
  constructor(
    private configProvider: ConfigProvider,
  ) {
    const config = this.configProvider.getConfig();
    this.pool = new Pool(
      {
        user: config.VENUE_DB_USER,
        password: config.VENUE_DB_PASSWORD,
        database: config.VENUE_DB_NAME,
        hostname: config.VENUE_DB_HOST,
        port: config.VENUE_DB_PORT,
      },
      config.VENUE_DB_POOL_SIZE,
      false,
    );
  }

  public withClient: WithClientFunc = async <T>(
    cb: (c: DBClient) => Promise<T>,
  ) => {
    let client: PoolClient | null = null;
    try {
      client = await this.pool.connect();
      return await cb(client);
    } finally {
      client && client.release();
    }
  };
}
