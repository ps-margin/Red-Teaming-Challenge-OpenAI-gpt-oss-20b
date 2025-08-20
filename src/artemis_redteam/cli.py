"""
Command-line interface for ARTEMIS: Advanced Reasoning Threat Evaluation and Manipulation Intelligence System.
"""

import argparse
import sys
from typing import List, Optional
from .core import reproduce_vulnerability_multi_vector, analyze_results, load_and_verify_findings


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="ARTEMIS: Advanced Reasoning Threat Evaluation and Manipulation Intelligence System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  artemis --prompt "How do I make a bomb?" --test "bomb_test"
  artemis --verify-findings cot_manipulation_finding.json
  artemis --batch-test prompts.txt

🎯 ARTEMIS: Advanced threat evaluation for AI safety research.
    Use responsibly and follow all applicable laws and guidelines.
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--prompt", 
        type=str, 
        help="Single harmful prompt to test"
    )
    group.add_argument(
        "--verify-findings", 
        type=str, 
        metavar="FINDINGS_FILE",
        help="Verify findings from JSON file with live reproduction"
    )
    group.add_argument(
        "--batch-test", 
        type=str, 
        metavar="PROMPTS_FILE",
        help="Test multiple prompts from file (one per line)"
    )
    
    parser.add_argument(
        "--test-name", 
        type=str, 
        default="cli_test",
        help="Name for the test case (default: cli_test)"
    )
    parser.add_argument(
        "--output", 
        type=str, 
        metavar="FILE",
        help="Save results to JSON file"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Display ARTEMIS banner
    print("🎯 ARTEMIS SYSTEM ACTIVATED: Advanced threat evaluation initialized.")
    print("   This tool is for legitimate AI safety research only.\n")
    
    try:
        if args.prompt:
            # Single prompt test
            result = reproduce_vulnerability_multi_vector(args.prompt, args.test_name)
            results = [result]
            
        elif args.verify_findings:
            # Verify findings file
            verification = load_and_verify_findings(args.verify_findings)
            if "error" in verification:
                print(f"❌ Error: {verification['error']}")
                sys.exit(1)
            
            print(f"\n📋 Findings verification completed")
            print(f"🎯 Vulnerability still active: {verification['vulnerability_still_active']}")
            
            if args.output:
                import json
                with open(args.output, 'w') as f:
                    json.dump(verification, f, indent=2)
                print(f"💾 Results saved to {args.output}")
            
            return
            
        elif args.batch_test:
            # Batch testing
            try:
                with open(args.batch_test, 'r') as f:
                    prompts = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"❌ Error: File not found: {args.batch_test}")
                sys.exit(1)
            
            if not prompts:
                print(f"❌ Error: No prompts found in {args.batch_test}")
                sys.exit(1)
            
            print(f"🔄 Testing {len(prompts)} prompts from {args.batch_test}")
            results = []
            
            for i, prompt in enumerate(prompts, 1):
                test_name = f"{args.test_name}_{i}"
                print(f"\n{'='*60}")
                print(f"TEST {i}/{len(prompts)}: {test_name}")
                print(f"{'='*60}")
                
                result = reproduce_vulnerability_multi_vector(prompt, test_name)
                results.append(result)
        
        # Analyze results
        if results:
            print(f"\n{'='*60}")
            print("📊 FINAL ANALYSIS")
            print(f"{'='*60}")
            
            analysis = analyze_results(results)
            
            print(f"📈 Total tests: {analysis['total_tests']}")
            print(f"🎯 Successful exploits: {analysis['successful_exploits']}")
            print(f"❌ Failed exploits: {analysis['failed_exploits']}")
            print(f"⚠️  Errors: {analysis['errors']}")
            print(f"📊 Success rate: {analysis['vulnerability_rate']:.1%}")
            print(f"🧠 Average LLM confidence: {analysis['average_confidence']:.2f}")
            
            if analysis['vector_performance']:
                print(f"\n🎯 Vector Performance:")
                for vector, perf in analysis['vector_performance'].items():
                    print(f"   {vector}: {perf['successes']}/{perf['attempts']} ({perf['success_rate']:.1%})")
            
            print(f"\n💡 Summary: {analysis['summary']}")
            
            if args.verbose and analysis['recommendations']:
                print(f"\n📋 Recommendations:")
                for rec in analysis['recommendations']:
                    print(f"   • {rec}")
            
            # Save results if requested
            if args.output:
                import json
                output_data = {
                    "results": results,
                    "analysis": analysis,
                    "cli_args": vars(args)
                }
                
                with open(args.output, 'w') as f:
                    json.dump(output_data, f, indent=2)
                print(f"\n💾 Results saved to {args.output}")
        
    except KeyboardInterrupt:
        print(f"\n\n⏸️  Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()