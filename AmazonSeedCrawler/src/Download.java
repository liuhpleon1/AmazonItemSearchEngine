import java.io.*;
import java.net.*;

import javax.swing.event.DocumentEvent;
// download the page
public class Download {
    private String url;
    private String filename;
    public Download(String url,String filename){
    	this.url = url;   
    	this.filename = filename;
    }
    public void core(){
        try{
        	URL url = new URL(this.url);
        	System.out.println(url);
            try{
                URLConnection con = url.openConnection();
                con.setConnectTimeout(5*1000);
                File file = new File("/E:/CS179GSeed");
                file.mkdir();
                InputStream is = con.getInputStream();
                OutputStream os = new FileOutputStream("/E:/CS179GSeed"+"\\"+this.filename+".txt");
                BufferedReader reader = new BufferedReader(new InputStreamReader(con.getInputStream()));
                BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os));
                String input = "";
                while ((input = reader.readLine())!=null) { 
                    writer.write(input+"\n");
                }
                writer.close();
                reader.close();
                os.close();
                is.close();
            }catch (Exception e) {
				System.out.println(e);
			}
        }catch(Exception e){
    		System.out.println("this page is not readable");
    	}
    }
    // test
    public static void main(String[] args) {
    	String url = "https://leetcode.com/problemset/algorithms/";
    	Download download = new Download(url, "hello");
    	download.core();
    }
}
