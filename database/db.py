
import sqlalchemy
from config import conf_parse

def init_mysql_by_conf(conf_file:str) -> sqlalchemy.engine.Engine:
    """
    初始化数据库连接
    :param conf_file:
    :return:
    """
    cfg = conf_parse.load_toml_config(conf_file)
    dsn = 'mysql+pymysql://{User}:{Password}@{Host}:{Port}/{DBName}?charset={Charset}&use_unicode=1'.format_map(cfg)
    engine = sqlalchemy.create_engine(dsn, pool_size=cfg['PoolSize'], pool_recycle=cfg['PoolRecycle'])
    return engine

if __name__ =='__main__':
    engine = init_mysql_by_conf('database.toml')
