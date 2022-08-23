package base;

public class ApiTestingPost {


    private String quoteNumber;
    private int id;
    private String userName;
    private String AccountTaxNumber;


/*
    public ApiTestingPost(String userName){

        this.userName=userName;

    }
    public ApiTestingPost(){

        this("userName");

    }

 */

    public String getAccountTaxNumber() {
        return AccountTaxNumber;
    }

    public void setAccountTaxNumber(String AccountTaxNumber) {
        this.AccountTaxNumber = AccountTaxNumber;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setQuoteNumber(String quoteNumber) {

        this.quoteNumber = quoteNumber;
    }

    public String getQuoteNumber() {
        return quoteNumber;
    }

}
