import java.util.Random;

/**
 * A utility class for generating random binary sequences.
 */
public class Main {
    
    /**
     * Generates a random 128-bit binary sequence as a string of '0's and '1's.
     * Each bit in the sequence is randomly generated with equal probability of being 0 or 1.
     * 
     * @return A string of length 128 representing the randomly generated binary sequence.
     */
    public static String generateRandomBinarySequence() {
        Random random = new Random();
        StringBuilder binaryString = new StringBuilder(128);
        
        for (int i = 0; i < 128; ++i) {
            binaryString.append(random.nextBoolean() ? '1' : '0');
        }
        
        return binaryString.toString();
    }
    
    /**
     * Main method that demonstrates the usage of the binary sequence generator.
     * Generates and prints a random 128-bit binary sequence.
     * 
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        String randomSequence = generateRandomBinarySequence();
        System.out.println("Random 128-bit binary sequence: " + randomSequence);
    }
}