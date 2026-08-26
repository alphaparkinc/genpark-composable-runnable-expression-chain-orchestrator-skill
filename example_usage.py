from client import ComposableRunnableExpressionChainOrchestratorClient

def main():
    client = ComposableRunnableExpressionChainOrchestratorClient()
    res = client.execute_lcel_runnable_graph('Cross-validate legal liabilities in merger contracts with fallback LLMs', True)
    print('Chain Run: ' + res['chain_execution_id'] + ' (' + str(res['chain_nodes_count']) + ' nodes)')
    print('TTFT Latency: ' + str(res['streaming_first_chunk_latency_ms']) + 'ms | Fallbacks: ' + str(res['fallback_branches_configured']))
    print('Topological Valid: ' + str(res['graph_topological_valid']) + ' | Manifest: ' + res['output_manifest_url'])

if __name__ == '__main__':
    main()
