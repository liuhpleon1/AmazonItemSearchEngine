public class Info {
	private String name;
	private String link;
	private String asin;
	private String piclink;
	private String price;
	private boolean availability;
	private boolean isPrime;
	private String type;
	private String introduction;
	public Info(String name,String link,String asin,String piclink,String price,boolean availability,boolean isPrime){
		this.name = name;
		this.link = link;
		this.asin = asin;
		this.piclink = piclink;
		this.price = price;
		this.availability = availability;
		this.isPrime = isPrime;
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
	public String picture(){
		return piclink;
	}
	public boolean available(){
		return availability;
	}
	public boolean prime(){
		return isPrime;
	}
	public String price(){
		return price;
	}
	public void addIntro(String a){
		introduction = a;
	}
	public String intro(){
		return introduction;
	}
}
