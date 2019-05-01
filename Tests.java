
public class Tests {

    public static void main(String[] args) {
        test1();
        test2();
    }

    public static void test1() {
        final int iterations = 1000;
        for (int i = 0; i < iterations; i++) {
            // Create random matrix
            boolean[][] matrix = MatrixLibrary.createRandomMatrix(10, 10, 0.8);
            
            // Search for rectangle
            if(FindRectangle.fastSearch(matrix) != FindRectangle.naiveSearch(matrix)) {
                // MatrixLibrary.printMatrix(matrix);
                // System.out.println(FindRectangle.fastSearch(matrix) + ", " + FindRectangle.naiveSearch(matrix) + ", " + i);
                System.out.println("TEST 1 FAILED");
                return;
            }
        }
        System.out.println("TEST 1 PASSED");
    }
    
    public static void test2() {
        // Create random matrix
        long startTime1 = System.currentTimeMillis();
        boolean[][] matrix = MatrixLibrary.createRandomMatrix(10000, 50000, 0.99999);
        long endTime1 = System.currentTimeMillis();
        System.out.println("EXECUTION TIME: " + (endTime1 - startTime1));
        
        // Fast search
        long startTime2 = System.currentTimeMillis();
        FindRectangle.fastSearch(matrix);
        long endTime2 = System.currentTimeMillis();
        System.out.println("EXECUTION TIME: " + (endTime2- startTime2));
        
        // Naive search
        long startTime3 = System.currentTimeMillis();
        //FindRectangle.naiveSearch(matrix);
        long endTime3 = System.currentTimeMillis();
        System.out.println("EXECUTION TIME: " + (endTime3 - startTime3));
    }

}
