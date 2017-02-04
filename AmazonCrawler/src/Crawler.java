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
			else firstnum = s.charAt(i)+firstnum; 
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
    		String asin = item.attr("data-asin");
    		Element e1 = null;
    		try{
    		    e1 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > div:nth-child(1) > a").get(0);	
    		}catch(Exception e){
    			
    		}
    		
    		String name = e1==null?null:e1.attr("title");
    		String link = e1==null?null:e1.attr("href");
    		
    		Element e2 = null;
    		try{
    		    e2 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-left > div > div > a > img").get(0);
    		    
    		}catch(Exception e){
    			
    		}
    		String piclink = e2==null?null:e2.attr("src");
    		   		
    		Element e3 = null;
    		String price = null;
    		try{
    	        e3 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(3) > div.a-column.a-span7 > div.a-row.a-spacing-none > a > span").get(0);
    	        price = e3.text();
    		}catch (Exception e) {
    			try{
                    e3 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(3) > div.a-column.a-span7 > div > div > a > span.a-size-base.a-color-base").get(0);
                    price = e3.text();
    			}catch (Exception error1) {
					try{
						e3 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(5) > div.a-column.a-span7 > div.a-row.a-spacing-none > a > span").get(0);
						price = e3.text();
					}catch (Exception error2) {
						
					}
				}
			}
    		
    	    boolean availability = price==null?false:true;
    	    
    	    Element e4 = null;
    	    try{
    	        e4 = item.select("div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(3) > div.a-column.a-span7 > div.a-row.a-spacing-none > i").get(0);
    	    }catch (Exception e) {
				// TODO: handle exception
			}
    		boolean isPrime = e4==null?false:true;
    		
    		if(e1!=null&&e2!=null&e3!=null&&e4!=null){
    			Info info = new Info(name, link, asin, piclink, price, availability, isPrime);
    		    seeds.add(info);
    		}
    		
    		System.out.println(i);
    		System.out.println(name);
    		System.out.println(link);
    		System.out.println(piclink);
    		System.out.println(price);
    		System.out.println(availability);
    		System.out.println(isPrime);
    		System.out.println(asin);
    		System.out.println("___________________________");
    		
    		try{
    		    Thread.sleep(200);
    		}catch(Exception e){
    			System.out.println("sleep 1 error");
    		}
    		i++;
    	}
    	return seeds;
    }
	
	public static void main(String args[]){
		Crawler crawler = new Crawler("https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dcomputers&field-keywords=desktop&rh=n%3A541966%2Ck%3Adesktop1");
	    crawler.getPage();  
	}
   
}


