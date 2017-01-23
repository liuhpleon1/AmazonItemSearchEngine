import org.jsoup.select.*;
import java.util.LinkedList;
import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.*;
import org.jsoup.parser.*;

public class Seed {
	// this is where we started
    private  String url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=node%3D"
    		+ "565108&field-keywords=computer&rh=n%3A172282%2Cn%3A5"
    		+ "41966%2Cn%3A13896617011%2Cn%3A565108%2Ck%3Acomputer";
    private boolean end = false;
    public LinkedList<Info> getPage(){
    	LinkedList<Info>seeds = new LinkedList<>();
    	try{
    		//connect to the website, we need to add userAgent or there is http 503 error
    		Document doc = Jsoup.connect(url).userAgent("Mozilla/5.0").timeout(100000).get();
    		int index = 0;
    		while(index<25){
    			String query = "#result_"+index;
    			Element element = null;
    			try{
    			     element = doc.select(query).get(0);
    			}catch(Exception exception){
    				System.out.println("end");
    				end = true;
    			}
    			if(end==true) break;
    			// get all the information from each element
    			// e1 contains name & link (title)
    			Element e1 = element.select("div > div > div > div.a-fixed-left-grid-col.a-col-right >"
    					+ " div.a-row.a-spacing-small > div:nth-child(1) > a").get(0);
    			String name = e1.attr("title");
    			String link = e1.attr("href");
    			String asin = element.attr("data-asin");
    			//e2 contains img src
    			Element e2 = element.select("div > div > div > div.a-fixed-left-grid-col.a-col-left > div > div > a > img").get(0);
    			String piclink = e2.attr("src");
    			System.out.println(index+1+" "+name+" "+asin);
    			System.out.println(link);
    			System.out.println(piclink);
    			Info info = new Info(name, link, asin, piclink);
    			seeds.add(info);
    		    Thread.sleep(200);
    		    index++;
    		}
    	}catch(Exception e){
    		System.out.println("error");
    		System.out.println(e);
    	}
    	return seeds;
    }
    
    public static void main(String args[]){
    	Seed seed = new Seed();
    	seed.getPage();
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