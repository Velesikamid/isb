import java.util.Random;

public class Main
{
    public static String generate_random_binary_sequence() {
        Random random = new Random();
        StringBuilder binary_string = new StringBuilder(128);
        
        for (int i = 0; i < 128; ++i) {
            binary_string.append(random.nextBoolean() ? '1' : '0');
        }
        
        return binary_string.toString();
    }
    
	public static void main(String[] args) {
		String random_sequence = generate_random_binary_sequence();
		System.out.println("Random 128-bit binary sequence: " + random_sequence);
	}
}