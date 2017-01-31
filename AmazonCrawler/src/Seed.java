import org.jsoup.select.*;
import java.util.LinkedList;
import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.*;
import org.jsoup.parser.*;
import org.json.*;
public class Seed {
 
    /*this part is to get all the items informations in each pages*/
    public LinkedList<Info> getPage(String url){
    	LinkedList<Info>seeds = new LinkedList<>();
    	try{
    		/*connect to the website, we need to add userAgent or there is http 503 error*/
    		Document doc = Jsoup.connect(url).userAgent("Mozilla/5.0").timeout(100000).get();
    		int index = 0;
			String query0 = "#s-results-list-atf";
			Element es = null;
			try{
			     es = doc.select(query0).get(0);
			}catch(Exception e){
				System.out.println("read query0 error");
				System.out.println(e);
			}
			Element first = es.child(0);
			String s = first.attr("id");
			int start = Integer.parseInt(s.substring(s.length()-2));
    		for(int i = start;i<start+25;i++){
    			// get all the information from each element
    			// e1 contains name & link (title)
    			Element element = doc.select("#result_"+i).get(0);
    			Element e1 = element.select("div > div > div > div.a-fixed-left-grid-col.a-col-right >"
    					+ " div.a-row.a-spacing-small > div:nth-child(1) > a").get(0);
    			String name = e1.attr("title");
    			String link = e1.attr("href");
    			String asin = element.attr("data-asin");
    			//e2 contains img src
    			Element e2 = element.select("div > div > div > div.a-fixed-left-grid-col.a-col-left > div > div > a > img").get(0);
    			String piclink = e2.attr("src");
    			System.out.println(name+" "+asin);
    			Info info = new Info(name, link, asin, piclink);
    			seeds.add(info);
    		    Thread.sleep(200);
    		    index++;
    		}
    	}catch(Exception e){
    		System.out.println("read query1 error");
    		System.out.println(e);
    	}
    	return seeds;
    }
    /*this part is to get next pages by reading the link in icon next*/
    public String getNext(String url){
    	String next = "";
    	try{
    	    Document doc = Jsoup.connect(url).userAgent("Mozilla/5.0").timeout(100000).get();
    	    next = doc.select("#pagnNextLink").get(0).attr("href");
    	}catch (Exception e) {
    		System.out.println("read nextlink error");
    		System.out.println(e);
		}
    	url = "https://www.amazon.com"+next;
    	System.out.println(url);
    	return url;
    }
    /*this part is to doing a loop to get all the informations start with starturl*/
    public LinkedList<Info> loop(String url){
    	LinkedList<Info>res = new LinkedList<>();
        for(int i=0;i<30;i++){
        	res.addAll(getPage(url));
        	url = getNext(url);
        	System.out.println("--------------------------------------");
        	try{
        	    Thread.sleep(1000);
        	}catch (Exception e) {
				// TODO: handle exception
			}
        }
        return res;
    }
    public static void main(String args[]){
    	String start = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=node%3D"
        		+ "565108&field-keywords=computer&rh=n%3A172282%2Cn%3A5"
        		+ "41966%2Cn%3A13896617011%2Cn%3A565108%2Ck%3Acomputer";
    	Seed seed = new Seed();
    	seed.loop(start);
    }
}
//build a class info to save the basic information that we downloaded online
class Info{
	String name;
	String link;
	String asin;
	String piclink;
	public Info(String name,String link,String asin,String piclink){
		this.name = name;
		this.link = link;
		this.asin = asin;
		this.piclink = piclink;
	}
	public String name(){
		return name;
	}
	public String link(){
		return link;
	}
	public String asin(){
		return asin;
	}
	public String piclink(){
		return piclink;
	}

}