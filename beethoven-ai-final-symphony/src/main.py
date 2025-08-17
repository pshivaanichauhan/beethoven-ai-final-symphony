from cv_analysis import analyze_score
from ml_authenticity import check_authenticity
from game_theory_collab import optimize_collaboration
from rpa_orchestration import orchestrate_workflow
from algorithms_rhythm import generate_rhythm

def run_demo():
    print("🎼 Running Beethoven AI Final Symphony Demo...")
    score_features = analyze_score("sample_score.png")
    authenticity = check_authenticity(score_features)
    collab = optimize_collaboration()
    orchestration = orchestrate_workflow()
    rhythm = generate_rhythm()

    print("\nDemo Results:")
    print("Score Features:", score_features)
    print("Authenticity Check:", authenticity)
    print("Collaboration Strategy:", collab)
    print("Orchestration Output:", orchestration)
    print("Rhythmic Pattern:", rhythm)

if __name__ == "__main__":
    run_demo()
