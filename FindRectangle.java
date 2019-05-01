// Author: Michael Wehar
// Description: This class finds a rectangle whose corners are 1's in an m by n Boolean matrix in O(mn) time.
// This algorithm is based on an approach from an upcoming paper to appear in CIAA 2019.
// Reference: Two-dimensional Pattern Matching against Basic Picture Languages (F. Mráz, D. Prusa, and M. Wehar)

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FindRectangle {
    
    public static boolean fastSearch(boolean[][] matrix) {
        // Check if the input is trivial
        if(MatrixLibrary.isTrivial(matrix)) {
            return false;
        }

        // Construct adjacency list for matrix or transposed matrix if there are fewer rows than columns
        boolean transposed;
        Map<Integer, List<Integer>> adjList;
        if(MatrixLibrary.getRows(matrix) >= MatrixLibrary.getCols(matrix)) {
            transposed = false;
            adjList = MatrixLibrary.getAdjacencyList(matrix);
        }
        else {
            transposed = true;
            adjList = MatrixLibrary.getAdjacencyListOfTranspose(matrix);
        }
        
        // Search for a rectangle whose corners are 1's
        int rows = adjList.size();
        Map<List<Integer>, Integer> pairs = new HashMap<>();
        for(int i = 0; i < rows; i++) {
            List<Integer> values = adjList.get(i);
            for(int j = 0; j < values.size(); j++) {
                for(int k = j + 1; k < values.size(); k++) {
                    List<Integer> pair = Arrays.asList(new Integer[] { values.get(j), values.get(k) });
                    if(pairs.containsKey(pair)) {
//                        // ##### START DEBUGGING #####
//                        if(transposed) {
//                            System.out.println("Rows: " + values.get(j) + ", " + values.get(k));
//                            System.out.println("Colums: " + pairs.get(pair) + ", " + i);
//                        }
//                        else {
//                            System.out.println("Rows: " + pairs.get(pair) + ", " + i);
//                            System.out.println("Colums: " + values.get(j) + ", " + values.get(k));
//                        }
//                        // ##### END DEBUGGING #####
                        return true;
                    }
                    else {
                        pairs.put(pair, i);
                    }
                }
            }
        }
        
        return false;
    }
    
    public static boolean naiveSearch(boolean[][] matrix) {
        int rows = MatrixLibrary.getRows(matrix);
        int cols = MatrixLibrary.getCols(matrix);
        for(int row1 = 0; row1 < rows; row1++) {
            for(int row2 = row1 + 1; row2 < rows; row2++) {
                for(int col1 = 0; col1 < cols; col1++) {
                    for(int col2 = col1 + 1; col2 < cols; col2++) {
                        if(matrix[row1][col1] && matrix[row1][col2] && matrix[row2][col1] && matrix[row2][col2]) {
                            // System.out.println(row1 + "," + row2 + "," + col1 + "," + col2);
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
    
}
