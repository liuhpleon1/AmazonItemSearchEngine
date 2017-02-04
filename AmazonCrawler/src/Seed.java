/*Haopeng Liu 2/3/2017*/
import java.io.*;
import org.jsoup.Jsoup;
import org.jsoup.nodes.*;
public class Seed {
    /*this part is to get next link informations in each pages*/
    public String getNext(String linkhref){
    	String next = "";
    	System.out.println(linkhref);
    	try{
    	    Document doc = Jsoup.connect(linkhref).userAgent("Mozilla/5.0").timeout(1000000).get();
    	    next = doc.select("#pagnNextLink").get(0).attr("href");
    	}catch (Exception e) {
    		System.out.println("read nextlink error(may be reach last)");
    		System.out.println(e);
		}
    	linkhref = "https://www.amazon.com"+next;
    	return linkhref;
    }
    /*this part is to doing a loop to get all the informations start with start link*/
    public void loop(String link,String name,int index){
    	int i = 0;
    	try{
    	 File file = new File("/E:/CS179GSeed/"+name+"/");
         file.mkdir();
         FileWriter writer = new FileWriter("/E:/CS179GSeed/"+name+"/"+name+index+".txt",true);
         while(i<=600){
        	 if(i!=0&&i%20==0){
        		 writer.close();
        		 index++;
        		 writer = new FileWriter("/E:/CS179GSeed/"+name+"/"+name+index+".txt",true);
        	 }
        	 else{
                 try{
        	         writer.write(link+"\n");
        	         link = getNext(link);    
        	        Thread.sleep(1000);
        	     }catch (Exception e) {
        	     	System.out.println("sleep error or write error");
        		    System.out.println(i);
        		    System.out.println(e);
        		    break;
		     	}
        	 }
        	 i++;
        }  
  	    writer.close();
    	}catch(IOException e){
    		System.out.println(e);
    	}
    	
    }
    public static void main(String args[]){
    	String start = ""
    			+ "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dcomputers&field-keywords=laptop&rh=n%3A541966%2Ck%3Alaptop"
    			+"";
    	Seed seed = new Seed();
    	seed.loop(start,"laptop",1);
    }
}