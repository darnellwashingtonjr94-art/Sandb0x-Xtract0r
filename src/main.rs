use clap::{Parser, Subcommand};

// Import your library modules
#[cfg(feature = "orchestrator")]
use sandb0x_xtract0r::orchestrator;
#[cfg(feature = "extractors")]
use sandb0x_xtract0r::extractors;

#[derive(Parser)]
#[command(name = "Xtract0r")]
#[command(about = "Sandbox extraction and orchestration engine CLI")]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Bootstraps and controls the sandbox environment
    Orchestrate {
        /// The target environment to spin up
        #[arg(short, long)]
        target: String,
    },
    /// Extracts payloads or telemetry from a finished run
    Extract {
        /// Filepath to the sandbox output
        #[arg(short, long)]
        path: String,
    }
}

fn main() {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Orchestrate { target } => {
            println!("Starting orchestrator for target: {}", target);

            #[cfg(feature = "orchestrator")]
            orchestrator::run_sandbox(target); // Assuming this function takes a target string
        }
        Commands::Extract { path } => {
            println!("Running extractors on path: {}", path);

            #[cfg(feature = "extractors")]
            extractors::parse_output(path); // Assuming this function takes a path string
        }
    }
}
