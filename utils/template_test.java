// ============================================================================
// Local Test Runner
// Copy and append this block to the bottom of your solution file.
// Compile & run: javac <file>.java && java -ea Main
// (-ea enables assert statements)
// NOTE: java.util.* is already imported at the top of template.java,
// so do not add imports here.
// ============================================================================

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // --------------------------------------------------------------------
        // Option A: Direct assertions (Quick & Simple)
        // --------------------------------------------------------------------
        // Example:
        // assert Arrays.equals(sol.twoSum(new int[]{2, 7, 11, 15}, 9), new int[]{0, 1});
        // System.out.println("Test 1: PASSED");

        // --------------------------------------------------------------------
        // Option B: Table-driven test cases (Scalable for multiple inputs)
        // --------------------------------------------------------------------
        /*
        int[][] inputs   = { {2, 7, 11, 15}, {3, 2, 4}, {3, 3} };
        int[]   targets  = { 9, 6, 6 };
        int[][] expected = { {0, 1}, {1, 2}, {0, 1} };

        int passed = 0;
        for (int i = 0; i < inputs.length; i++) {
            int[] actual = sol.twoSum(inputs[i].clone(), targets[i]);
            if (Arrays.equals(actual, expected[i])) {
                System.out.println("Test " + (i + 1) + ": PASSED");
                passed++;
            } else {
                System.out.println("Test " + (i + 1) + ": FAILED (Expected: "
                    + Arrays.toString(expected[i]) + ", Got: " + Arrays.toString(actual) + ")");
            }
        }
        System.out.println("Results: " + passed + "/" + inputs.length + " passed.");
        */
    }
}
