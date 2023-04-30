import java.util.HashMap;

public class Node {

    public static int Estimativa;
    public static int Peso;
    public static int ValorAtual;
    public static int Profundidade;
    HashMap<Integer, double[]> valuesDict;
    public static int[] TakenAtual;
    Node left;
    Node right;

    public Node(int estInput, int pesoInput, int valorInput, int[] taken, int profundidade, HashMap<Integer, double[]> valuesDictInput){
        Estimativa = estInput;
        Peso = pesoInput;
        ValorAtual = valorInput;
        TakenAtual = taken;
        Profundidade = profundidade;
        valuesDict = valuesDictInput;
        right = null;
        left = null;
    }


}
