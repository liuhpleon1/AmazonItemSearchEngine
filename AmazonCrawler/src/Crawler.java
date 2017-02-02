import org.jsoup.Jsoup;
import org.jsoup.nodes.*;
import org.jsoup.select.*;
import java.io.*;
import java.util.LinkedList;
import java.util.List;
/*the crawling method is first save the link, vinnubmer and info as a Json file*/
public class Crawler {
	private String link;
	public Crawler(String link){
		this.link = link;
	}
	/*get items information including link, name, asin and piclink*/
	public LinkedList<Info> getPage(){
    	LinkedList<Info>seeds = new LinkedList<>();
    	Document doc = null;
    	try{
            doc = Jsoup.connect(link).userAgent("Mozilla/5.0").timeout(10000).get();
		}catch(Exception e){
            System.out.println("init error");
			System.out.println(e);
		}
    	/*connect to the website, we need to add userAgent or there is http 503 error*/
		String getlist = "#s-results-list-atf";
		Element itemslist = null;
		try{
		     itemslist = doc.select(getlist).get(0);
		}catch(Exception e){
			System.out.println("read item list error");
			System.out.println(e);
		}
		Element first = itemslist.child(0);
		String s = first.attr("id");
		String firstnum = "";
		for(int i= s.length()-1;i>=0;i--){
			if(s.charAt(i)<'0'||s.charAt(i)>'9') break;
			else firstnum = firstnum+s.charAt(i); 
		}
		int start = Integer.parseInt(firstnum);
		int i = start;
		Element item = null;
		try{
		    item = doc.select("#result_"+i).get(0);
		}catch(Exception e){
				System.out.println("read result error");
		}
    	while(item!=null){
    		// get all the information from each element
    		// e1 contains name & link (title)
    		try{
    		    item = doc.select("#result_"+i).get(0);
    		}catch (Exception e) {
    			System.out.println("read complete");
    			break;
			}
    		Element content = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > div:nth-child(1) > a").get(0);		
    		String name = content.attr("title");
    		String link = content.attr("href");
    		String asin = item.attr("data-asin");
      		//e2 contains img src
    		Element e2 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-left > div > div > a > img").get(0);
    		String piclink = e2.attr("src");
    		Info info = new Info(name, link, asin, piclink);
    		seeds.add(info);
    		try{
    		    Thread.sleep(200);
    		}catch(Exception e){
    			System.out.println("sleep 1 error");
    		}
    		System.out.println(i+"."+name+" "+asin);
    		i++;
    	}
    	return seeds;
    }
   
}
// we use the class info to collect and restore the data that we use a single thread to download;


