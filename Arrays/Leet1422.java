
//011101
// left = "0" and right = "11101", score = 1 + 4 = 5 
// left = "01" and right = "1101", score = 1 + 3 = 4 
// left = "011" and right = "101", score = 1 + 2 = 3 
// left = "0111" and right = "01", score = 1 + 1 = 2 
// left = "01110" and right = "1", score = 2 + 1 = 3

class Main {
    public static void main(String[] args) {
        String s = "011101";
        int zero=0;
        int one=0;
        int tempzero=0;
        int tempone=0;
        int sum=0;
        int maxsum=0;
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i)=='0'){
                zero++;
            }else{
                one++;
            }
            // Print current character
            // System.out.print(s.charAt(i) + " ");
        }
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i)=='0'){
                tempzero+=1;
            }else{
                tempone+=1;
            }
            sum+=tempzero;
            sum+=((s.length()-1-i)+(one-tempone));
            if(sum>maxsum){
                maxsum=sum;
            }
            sum=0;
        }
        System.out.println(maxsum);
    }
}