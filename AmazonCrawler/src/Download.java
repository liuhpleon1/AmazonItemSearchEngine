import java.io.*;
import java.net.*;

import javax.swing.event.DocumentEvent;
// download the page
public class Download {
    private String url;
    private String filename;
    public Download(String url,String filename){
    	this.url = url;    
    }
    public void core(){
    	if(filename.length()>0){
    	try{
        	URL url = new URL(this.url);
        	System.out.println(url);
            try{
                OutputStream os1 = new FileOutputStream("/E:/CS242Link"+"\\"+this.filename+".txt");
                BufferedWriter writer1 = new BufferedWriter(new OutputStreamWriter(os1));
                writer1.write(url.toString());
                System.out.println(url.toString());
                writer1.close();
                os1.close();
            }catch (Exception e) {
				System.out.println(e);
			}
            URLConnection con = url.openConnection();
            con.setConnectTimeout(5*1000);
            InputStream is = con.getInputStream();
            OutputStream os = new FileOutputStream("/E:/CS242DATA"+"\\"+this.filename+".html");
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

        }catch(Exception e){
    		System.out.println("this page is not readable");
    	}
    	}
    }
    // test
    public static void main(String[] args) {
    	String url = "https://leetcode.com/problemset/algorithms/";
    	Download download = new Download(url, "hello");
    	download.core();
    }
}
