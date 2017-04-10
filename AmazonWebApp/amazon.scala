val dfs=sqlContext.read.json("pre_index.json")

val title = dfs.select("title")
val strTitle = title.map(row=>row.toString())	//Converts to string
val wordTitle = strTitle.map(line=>line.split(" "))

val asin = dfs.select("asin")	//Selects asin
val strAsin = asin.map(row=>row.toString())	//Converts to string

val wordMap = wordTitle.saveAsTextFile("Amazon")
