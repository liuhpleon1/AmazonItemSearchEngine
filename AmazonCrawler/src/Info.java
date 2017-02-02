public class Info {
	String name;
	String link;
	String asin;
	String piclink;
	String price;
	String availability;
	/*basic construction method*/
	public Info(String name,String link,String asin,String piclink){
		this.name = name;
		this.link = link;
		this.asin = asin;
		this.piclink = piclink;
	}
	/*construction with price*/
	public Info(String name,String link,String asin,String piclink,String price){
		this.name = name;
		this.link = link;
		this.asin = asin;
		this.piclink = piclink;
		this.price = price;
	}
	/*construction with availability*/
	public Info(String name,String link,String asin,String piclink,String price,String availability){
		this.name = name;
		this.link = link;
		this.asin = asin;
		this.piclink = piclink;
		this.price = price;
		this.availability = availability;
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
