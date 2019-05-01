import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MatrixLibrary {

    public static int getRows(boolean[][] matrix) {
        return matrix.length;
    }
    
    public static int getCols(boolean[][] matrix) {
        return matrix[0].length;
    }
    
    public static boolean isTrivial(boolean[][] matrix) {
        return getRows(matrix) < 2 || getCols(matrix) < 2;
    }
    
    public static boolean[][] transpose(boolean[][] matrix){
        int rows = getRows(matrix);
        int cols = getCols(matrix);
        boolean[][] newMatrix = new boolean[cols][rows];
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                newMatrix[j][i] = matrix[i][j];
            }
        }
        return newMatrix;
    }
    
    public static Map<Integer, List<Integer>> getAdjacencyList(boolean[][] matrix){
        int rows = getRows(matrix);
        int cols = getCols(matrix);
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for(int i = 0; i < rows; i++) {
            adjList.put(i, new ArrayList<Integer>());
            for(int j = 0; j < cols; j++) {
                if(matrix[i][j]) {
                    adjList.get(i).add(j);
                }
            }
        }
        return adjList;
    }
    
    // Create a matrix with random entries
    public static boolean[][] createRandomMatrix(int rows, int cols, double thresh) {
        boolean[][] matrix = new boolean[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = Math.random() >= thresh;
            }
        }
        return matrix;
    }
    
    // Print the entries of a matrix
    public static void printMatrix(boolean[][] matrix) {
        int rows = getRows(matrix);
        int cols = getCols(matrix);
        System.out.println(rows + " by " + cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if(matrix[i][j]) {
                    System.out.print(1);
                }
                else {
                    System.out.print(0);
                }
                if(j < cols - 1) {
                    System.out.print("\t");
                }
            }
            System.out.println();
        }
        System.out.println();
    }
    
}
