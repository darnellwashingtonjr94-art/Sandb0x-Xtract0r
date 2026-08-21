use clap::{Parser, Subcommand};

// Import your library modules
#[cfg(feature = "orchestrator")]
use sandb0x_xtract0r::orchestrator;
#[cfg(feature = "extractors")]
use sandb0x_xtract0r::extractors;

#[derive(Parser)]
#[command(name = "xtract0r")]
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
    },
}
