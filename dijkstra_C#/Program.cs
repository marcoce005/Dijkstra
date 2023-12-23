namespace Name {
    class dijkstra {
        class grafo { 
            public int n_nodi {get; set;}
            public List<int> ?visitati {get; set;}
            public List<List<int>> ?percorsi {get;set;}

            grafo(int n_vertici) {
                n_nodi = n_vertici;

                List<int> x = new List<int>();
                for (int i = 0; i < n_vertici; i++)
                    x.Add(-1);

                for (int j = 0; j < n_vertici; j++)
                    percorsi.Add(x);
            }

            void add_edge() {

            }
        }

        static void main() {

        }
    }
}