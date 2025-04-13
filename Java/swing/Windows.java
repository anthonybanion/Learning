/* Description: Shows a window with the title "Windows".
 * Filename: Windows.java
 * Creation date: 17/03/2025*/


package swing;
import javax.swing.JFrame;


public class Windows extends JFrame {
    public Windows() {
        super("Windows");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
        setVisible(true);

    }

    public static void main(String[] args) {
        new Windows();
    }
}

