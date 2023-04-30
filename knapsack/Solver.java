import java.io.*;
import java.util.*;

/**
 * The class <code>Solver</code> is an implementation of a greedy algorithm to solve the knapsack problem.
 *
 */
public class Solver {
    
    /**
     * The main class
     */
    public static void main(String[] args) {
        try {
            solve(args);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    /**
     * Read the instance, solve it, and print the solution in the standard output
     */

    public static void solve(String[] args) throws IOException {

        String fileName = null;
        
        // get the temp file name
        for(String arg : args){
            if(arg.startsWith("-file=")){
                fileName = arg.substring(6);
            } 
        }
        if(fileName == null)
            return;
        
        // read the lines out of the file
        List<String> lines = new ArrayList<String>();

        try (BufferedReader input = new BufferedReader(new FileReader(fileName))) {
            String line = null;
            while ((line = input.readLine()) != null) {
                lines.add(line);
            }
        }

        // parse the data in the file
        String[] firstLine = lines.get(0).split("\\s+");
        int items = Integer.parseInt(firstLine[0]);
        int capacity = Integer.parseInt(firstLine[1]);

        int[] values = new int[items];
        int[] weights = new int[items];
        int value = 0;
        int weight = 0;
        int[] taken = new int[items];
        int estimativa = 0;

        HashMap<Integer, double[]> valuesDict = new HashMap<Integer, double[]>();

        for (int i = 0; i < items; i++) {
            String line = lines.get(i + 1);
            String[] parts = line.split("\\s+");
        
            values[i] = Integer.parseInt(parts[0]);
            weights[i] = Integer.parseInt(parts[1]);

            valuesDict.put(i, new double[]{values[i], weights[i], (float) values[i] / weights[i]});
        }

        List<Map.Entry<Integer, double[]>> list = new ArrayList<Map.Entry<Integer, double[]>>(valuesDict.entrySet());

        list.sort(new Comparator<Map.Entry<Integer, double[]>>() {
            public int compare(Map.Entry<Integer, double[]> o1, Map.Entry<Integer, double[]> o2) {
                double[] arr1 = o1.getValue();
                double[] arr2 = o2.getValue();
                double last1 = arr1[arr1.length - 1];
                double last2 = arr2[arr2.length - 1];
                return Double.compare(last2, last1);
            }
        });

        HashMap<Integer, double[]> sortedMap = new LinkedHashMap<Integer, double[]>();
        for (Map.Entry<Integer, double[]> entry : list) {
            sortedMap.put(entry.getKey(), entry.getValue());
        }

        ///////////////



        /*
        for (Integer key : sortedMap.keySet()) {
            if(weight + sortedMap.get(key)[1] <= capacity){
                estimativa += sortedMap.get(key)[0];
                weight += sortedMap.get(key)[1];
            } else if (weight != capacity) {
                int diference = capacity - weight;

                double percent = (double) diference/sortedMap.get(key)[1];

                weight = capacity;

                estimativa += sortedMap.get(key)[0] * percent;
            }
        }

        weight = 0;
         */

        for (Integer key : sortedMap.keySet()) {
            if(weight + sortedMap.get(key)[1] <= capacity){
                value += sortedMap.get(key)[0];
                weight += sortedMap.get(key)[1];
                taken[key] = 1;
            } else {
                taken[key] = 0;
            }
        }

        // a trivial greedy algorithm for filling the knapsack
        // it takes items in-order until the knapsack is full

        /*
        for(int i=0; i < items; i++){
            if(weight + weights[i] <= capacity){
                taken[i] = 1;
                value += values[i];
                weight += weights[i];
            } else {
                taken[i] = 0;
            }
        }
         */
        
        // prepare the solution in the specified output format
        System.out.println(value+" 0");
        for(int i=0; i < items; i++){
            System.out.print(taken[i]+" ");
        }
        System.out.println("");        
    }
}