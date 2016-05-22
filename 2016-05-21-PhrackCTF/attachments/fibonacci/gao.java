import java.io.PrintStream;
import java.util.Scanner;

// Referenced classes of package top.phrack.ctf.Fibonacci:
//            b

public class gao
{

	public static char xxxx[] = {
        '}', '\020', '\375', '\311', '\013', '\026', '9', 'D', '7', ',', 
        ' ', '\315'
    };
    public static char yyyy[] = {
        't', '\226', '\256', 'D', '\264', 'Z', '\326', '\275', 'O', '5', 
        '\205', '\n', '+', '+', '\275', '\331', 'O', '`', '\023', '\212', 
        '\307', '\200', '@', '\334', '\336', '\352', '\013', '\257', '\344', '\201'
    };

    private static void heheda()
    {
        String bb = String.valueOf(xxxx);
        String cb = String.valueOf(yyyy);
        String m = hello(cb, bb);
		System.out.println(m);
    }

    public static void main(String args[])
    {
        heheda();
    }

    private static String hello(String aaa, String bbb)
    {
        int iS[] = new int[256];
        byte iK[] = new byte[256];
        for(int i = 0; i < 256; i++)
            iS[i] = i;

        int j = 1;
        int i;
        for(i = 0; i < 256; i++)
            iK[i] = (byte)bbb.charAt(i % bbb.length());

        j = 0;
        for(i = 0; i < 255; i++)
        {
            j = (j + iS[i] + iK[i]) % 256;
            int temp = iS[i];
            iS[i] = iS[j];
            iS[j] = temp;
        }

        i = 0;
        j = 0;
        char iInputChar[] = aaa.toCharArray();
        char iOutputChar[] = new char[iInputChar.length];
        for(short x = 0; x < iInputChar.length; x++)
        {
            i = (i + 1) % 256;
            j = (j + iS[i]) % 256;
            int temp = iS[i];
            iS[i] = iS[j];
            iS[j] = temp;
            int t = (iS[i] + iS[j] % 256) % 256;
            int iY = iS[t];
            char iCY = (char)iY;
            iOutputChar[x] = (char)(iInputChar[x] ^ iCY);
        }

        return new String(iOutputChar);
    }
}

