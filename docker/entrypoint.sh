#!/bin/sh

echo $DATABASE_SSLCERT > /ssl/postgresql.crt
echo $DATABASE_SSLKEY > /ssl/postgresql.key
echo $DATABASE_ROOTCERT > /ssl/root.crt

jet_bridge --environment_type=docker --media_root=/jet/jet_media --use_default_config=project,token,address,config
