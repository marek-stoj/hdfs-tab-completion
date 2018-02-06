# hdfs-tab-completion
A simple utility that makes interacting with HDFS from command-line a little bit more convenient.

Let’s say we have an HDFS directory: `/user/someuser/somedir/`
 
We’d like to have TAB completion in the command line when writing HDFS commands. The utility mirrors the directory structure (with empty files inside) in the local file system (in your current working directory). You run the tool like this:

```
./hdfs-tab-completion.py /user/someuser/somedir/
```
 
It will create the `somedir` directory so that you will be able to use TAB in commands like these:
 
```
hdfs dfs –ls somedir/someotherdir/...
```
