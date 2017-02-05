/*Haopeng Liu 2/3/2017*/
import java.io.*;

import javax.print.Doc;

import org.jsoup.Jsoup;
import org.jsoup.nodes.*;
public class Seed {
    /*this part is to get next link informations in each pages*/
	/*
	"Mozilla/5.0  AppleWebKit/537.36  Chrome/56.0.2924.87 Safari/537.36"
	*/
    public String getNext(String linkhref){
    	String next = "";
    	System.out.println(linkhref);
    	Document doc = null;
    	try{
    	     doc = Jsoup.connect(linkhref).userAgent("AppleWebKit/537.36").timeout(1000000).get();
    	    try{
    	    next = doc.select("#pagnNextLink").get(0).attr("href");
    	    }catch (Exception e) {
				// TODO: handle exception
    	    	System.out.println(next.equals(""));
    	    	System.out.println("select nextlink error(may be reach last)");
    	    	System.out.println(e);
			}
    	}catch (Exception e) {
    		System.out.println("read nextlink error(may be reach last)");
    		System.out.println(e);
		}
    	linkhref = "https://www.amazon.com"+next;
    	return linkhref;
    }
    
    /*this part is to doing a loop to get all the informations start with start link*/
    public void loop(String link,String name){
    	int i = 0;
    	try{
         FileWriter writer = new FileWriter("/E:/CS179GSeed/"+name+".txt",true);
         while(i<=400){
        	 
                 try{
        	         writer.write(link+"\n");
        	         link = getNext(link); 
        	         if(link.equals("https://www.amazon.com")) break;
        	         Thread.sleep(200);
        	     }catch (Exception e) {
        	     	System.out.println("sleep error or write error");
        	     	writer.close();
        		    System.out.println(i);
        		    System.out.println(e);
        		    break;
		     	}
        	 }
        	 i++;
         
  	    writer.close();
    	}catch(IOException e){
    		System.out.println("write error");
    		System.out.println(e);
    	}
    	
    }
    
    public static void main(String args[]){
    	String start = ""
    			+ 
    			"https://www.amazon.com/s/ref=nb_sb_noss_2?url=node%3D193870011&field-keywords=montherboard"
    			+
    			"";
    	Seed seed = new Seed();
    	seed.loop(start,"motherboard");
    }
}