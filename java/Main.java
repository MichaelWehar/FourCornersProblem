
public class Main {

    public static void main(String[] args) {
        // Create random matrix
        boolean[][] matrix = MatrixLibrary.createRandomMatrix(10, 10, 0.8);

        // Print matrix
        MatrixLibrary.printMatrix(matrix);

        // Search for rectangle
        if (FindRectangle.fastSearch(matrix)) {
            System.out.println("FOUND");
        } else {
            System.out.println("NOT FOUND");
        }
    }

}
