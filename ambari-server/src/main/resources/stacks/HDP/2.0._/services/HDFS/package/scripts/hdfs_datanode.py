"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
from utils import service


def datanode(action=None):
  import params

  if action == "configure":
    Directory(params.dfs_domain_socket_dir,
              recursive=True,
              mode=0750,
              owner=params.hdfs_user,
              group=params.user_group)
    Directory(params.dfs_data_dir,
              recursive=True,
              mode=0755,
              owner=params.hdfs_user,
              group=params.user_group)

  if action == "start":
    service(
      action=action, name="datanode",
      user=params.hdfs_user,
      create_pid_dir=True,
      create_log_dir=True,
      keytab=params.dfs_datanode_keytab_file,
      principal=params.dfs_datanode_kerberos_principal
    )
  if action == "stop":
    service(
      action=action, name="datanode",
      user=params.hdfs_user,
      create_pid_dir=True,
      create_log_dir=True,
      keytab=params.dfs_datanode_keytab_file,
      principal=params.dfs_datanode_kerberos_principal
    )
