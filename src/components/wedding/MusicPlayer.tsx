import { motion, AnimatePresence } from "framer-motion";
import { Music, VolumeX } from "lucide-react";
import { useEffect, useRef, useState } from "react";

interface MusicPlayerProps {
  autoPlayTrigger?: boolean;
}

export function MusicPlayer({ autoPlayTrigger }: MusicPlayerProps) {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    const audio = new Audio("/videoplayback.mp3");
    audio.loop = true;
    audio.volume = 0.7;
    audio.preload = "auto";
    audioRef.current = audio;

    const handlePlay = () => setIsPlaying(true);
    const handlePause = () => setIsPlaying(false);

    audio.addEventListener("play", handlePlay);
    audio.addEventListener("pause", handlePause);

    return () => {
      audio.removeEventListener("play", handlePlay);
      audio.removeEventListener("pause", handlePause);
      audio.pause();
      audioRef.current = null;
    };
  }, []);

  // When user opens the invitation, start playing the looped BGM
  useEffect(() => {
    if (autoPlayTrigger && audioRef.current && !isPlaying) {
      audioRef.current.play().catch(() => {
        // Autoplay may be restricted on some devices until explicit toggle
      });
    }
  }, [autoPlayTrigger, isPlaying]);

  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play().catch((err) => {
        console.warn("Audio play error:", err);
      });
    }
  };

  return (
    <motion.button
      onClick={togglePlay}
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      whileHover={{ scale: 1.08 }}
      whileTap={{ scale: 0.92 }}
      className="fixed right-4 top-4 z-40 flex h-11 w-11 items-center justify-center rounded-full border border-gold/40 bg-emerald-ink/85 text-gold shadow-gold backdrop-blur-md transition-colors hover:border-gold hover:bg-emerald-ink focus:outline-none"
      aria-label={isPlaying ? "Pause background music" : "Play background music"}
      title={isPlaying ? "Mute music" : "Play music"}
    >
      <AnimatePresence mode="wait" initial={false}>
        {isPlaying ? (
          <motion.div
            key="playing"
            initial={{ scale: 0.5, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.5, opacity: 0 }}
            className="flex items-center justify-center"
          >
            {/* Rotating vinyl-like music note */}
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ repeat: Infinity, duration: 4.5, ease: "linear" }}
              className="flex items-center justify-center"
            >
              <Music className="h-5 w-5" />
            </motion.div>
          </motion.div>
        ) : (
          <motion.div
            key="paused"
            initial={{ scale: 0.5, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.5, opacity: 0 }}
            className="flex items-center justify-center opacity-65"
          >
            <VolumeX className="h-5 w-5" />
          </motion.div>
        )}
      </AnimatePresence>
    </motion.button>
  );
}
