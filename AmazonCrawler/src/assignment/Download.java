package assignment;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import org.jsoup.*;
import org.jsoup.nodes.Document;
import org.jsoup.select.*;
import org.jsoup.nodes.*;
public class Download {
    public void crawler(){
    	String url = "http://www.ucr.edu/";
    	try{
        	File file = new File("E:/ucr.txt");
        	OutputStream os = new FileOutputStream(file);
        	BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os));
            Document docs = Jsoup.connect(url).get();
    	    Elements links = docs.select("body").get(0).getElementsByTag("a");
    	    for(Element link:links){
    	    	String href = link.attr("href");
    	    	if(href.length()>0){
    	    	    System.out.println(href);
    	    	    writer.write(href.toString()+"\n");
    	    	    Thread.sleep(300);
    	    	}
    	    }
    	    writer.close();
        }catch(Exception e){
        	System.out.println(e);
        }
    }
    public static void main(String args[]){
    	Download download = new Download();
    	download.crawler();
    }
    
}
