import java.util.List;
import org.json.*;
import org.json.simple.JSONObject;;
public class Jsonify {
	private List<Info>list;
	private String link;
	private boolean read;
	private JSONObject seed;
    public Jsonify(List<Info>list){
    	this.list = list;
    }
    public Jsonify(String link,boolean read){
    	this.link = link;
    	this.read = read;
    	seed = new JSONObject();
    }
    public void parserInfo(){
    	
    }
    public JSONObject JsonSeed(){
    	return seed;
    }
}
