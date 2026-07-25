# Exercise 1 - Hadoop Single Node Setup

## Objective
Install and configure Hadoop in Single Node mode on Ubuntu.

## Software Used
- Ubuntu (WSL)
- Java 11
- Hadoop 3.4.1

## Steps Performed
1. Installed Java.
2. Configured SSH.
3. Downloaded Hadoop.
4. Set Hadoop environment variables.
5. Configured:
   - core-site.xml
   - hdfs-site.xml
   - mapred-site.xml
   - yarn-site.xml
6. Formatted the NameNode.
7. Started HDFS.
8. Started YARN.
9. Verified services using JPS.

## Services Running
- NameNode
- DataNode
- SecondaryNameNode
- ResourceManager
- NodeManager

## Verification Commands

```bash
jps
hadoop version
hdfs dfsadmin -report
```

## Result

Hadoop Single Node Setup was completed successfully.
