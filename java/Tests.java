
public class Tests {

    public static void test1() {
        System.out.println("##### TEST 1 STARTED #####");
        // Create random matrix
        boolean[][] matrix = MatrixLibrary.createRandomMatrix(10, 10, 0.835);

        // Print matrix
        MatrixLibrary.printMatrix(matrix);

        // Search for rectangle
        if (FindRectangle.fastSearch(matrix)) {
            System.out.println("FOUND");
        } else {
            System.out.println("NOT FOUND");
        }
        System.out.println("##### TEST 1 FINISHED #####");
    }

    public static void test2() {
        System.out.println("##### TEST 2 STARTED #####");
        final int iterations = 1000;
        for (int i = 0; i < iterations; i++) {
            // Create random matrix
            boolean[][] matrix = MatrixLibrary.createRandomMatrix(10, 10, 0.835);

            // Search for rectangle
            if (FindRectangle.fastSearch(matrix) != FindRectangle.naiveSearch(matrix)) {
                // MatrixLibrary.printMatrix(matrix);
                // System.out.println(FindRectangle.fastSearch(matrix) + ", " +
                // FindRectangle.naiveSearch(matrix) + ", " + i);
                System.out.println("*** RESULTS DO NOT MATCH ***");
                System.out.println("##### TEST 2 FINISHED #####");
                return;
            }
        }
        System.out.println("*** ALL RESULTS MATCH ***");
        System.out.println("##### TEST 2 FINISHED #####");
    }

    public static void test3() {
        System.out.println("##### TEST 3 STARTED #####");

        // Create random matrix
        System.out.println("TASK 1");
        long startTime1 = System.currentTimeMillis();
        boolean[][] matrix = MatrixLibrary.createRandomMatrix(500, 5000, 0.99919);
        // Example case where the optimization with computing the adjacency list of
        // the transpose significantly improves the runtime:
        // boolean[][] matrix = MatrixLibrary.createRandomMatrix(50, 5000000, 0.999);
        long endTime1 = System.currentTimeMillis();
        System.out.println("* EXECUTION TIME: " + (endTime1 - startTime1));

        // Fast search
        System.out.println("TASK 2");
        long startTime2 = System.currentTimeMillis();
        System.out.println("* SEARCH RESULT: " + FindRectangle.fastSearch(matrix));
        long endTime2 = System.currentTimeMillis();
        System.out.println("* EXECUTION TIME: " + (endTime2 - startTime2));

        // Naive search
        System.out.println("TASK 3");
        long startTime3 = System.currentTimeMillis();
        System.out.println("* SEARCH RESULT: " + FindRectangle.naiveSearch(matrix));
        long endTime3 = System.currentTimeMillis();
        System.out.println("* EXECUTION TIME: " + (endTime3 - startTime3));

        System.out.println("##### TEST 3 FINISHED #####");
    }

}
