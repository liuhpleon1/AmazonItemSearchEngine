import java.util.LinkedList;
import org.jsoup.Jsoup;
import org.jsoup.nodes.*;
public class Seed {
    /*this part is to get next link informations in each pages*/
    public String getNext(String linkhref){
    	String next = "";
    	System.out.println(linkhref);
    	try{
    	    Document doc = Jsoup.connect(linkhref).userAgent("Mozilla/5.0").timeout(1000).get();
    	    next = doc.select("#pagnNextLink").get(0).attr("href");
    	}catch (Exception e) {
    		System.out.println("read nextlink error(many be reach last)");
    		System.out.println(e);
		}
    	linkhref = "https://www.amazon.com"+next;
    	return linkhref;
    }
    /*this part is to doing a loop to get all the informations start with start link*/
    public LinkedList<String> loop(String link){
    	LinkedList<String>res = new LinkedList<>();
        for(int i=0;i<30;i++){
        	link = getNext(link);
        	res.add(link);
        	try{
        	    Thread.sleep(1000);
        	}catch (Exception e) {
        		System.out.println("read next sleep error");
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