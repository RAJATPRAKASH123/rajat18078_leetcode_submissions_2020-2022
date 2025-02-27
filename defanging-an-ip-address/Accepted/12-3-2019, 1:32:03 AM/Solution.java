// https://leetcode.com/problems/defanging-an-ip-address

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;
class Solution {
    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;
        public FastReader()
        {
            br = new BufferedReader( new InputStreamReader(System.in));
        }
        String next()
        {
            while ( st == null || !st.hasMoreElements())
            {
                try
                {
                    st = new StringTokenizer( br.readLine());
                }
                catch( IOException e )
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt()
        {
            return Integer.parseInt(next());
        }
        long nextLong()
        {
            return  Long.parseLong(next());
        }
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
        String nextLine()
        {
            String str = "";
            try
            {
                str = br.readLine();
            }
            catch(IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
    
    public String defangIPaddr(String str){
        
        String a = "";
        
        for ( int i = 0; i < str.length(); i++)
        {
            if ( str.charAt(i) == '.')
            {
                a += "[.]";
            }else{
                a += str.charAt(i);
            }
        }
        return a;
    }
}