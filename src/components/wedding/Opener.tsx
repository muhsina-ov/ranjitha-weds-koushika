import { AnimatePresence, motion } from "framer-motion";
import { useState } from "react";
import { Aurora } from "@/components/Aurora";
import { Petals } from "./Petals";
import { wedding } from "./data";

/**
 * Full-screen "seal + curtain" opener. Tapping the wax seal splits the
 * gold curtains and reveals the invitation.
 */
export function Opener({ onOpen }: { onOpen: () => void }) {
  const [opening, setOpening] = useState(false);

  const open = () => {
    if (opening) return;
    setOpening(true);
    window.setTimeout(onOpen, 1500);
  };

  return (
    <motion.div
      className="fixed inset-0 z-50 flex items-center justify-center overflow-hidden"
      exit={{ opacity: 0 }}
      transition={{ duration: 0.5 }}
    >
      {[-1, 1].map((dir) => (
        <motion.div
          key={dir}
          className="bg-emerald-ink absolute inset-y-0 w-[51%] overflow-hidden"
          style={{ [dir === -1 ? "left" : "right"]: 0 }}
          animate={opening ? { x: `${dir * 105}%` } : { x: 0 }}
          transition={{ duration: 1.3, ease: [0.76, 0, 0.24, 1] }}
        >
          <Aurora intensity={0.55} />
          <div
            className="pointer-events-none absolute inset-0 opacity-20"
            style={{
              backgroundImage: "url('/images/mandala-texture.jpg')",
              backgroundSize: "cover",
              backgroundPosition: dir === -1 ? "right center" : "left center",
            }}
          />
          <div
            className="absolute inset-y-0 w-[2px]"
            style={{
              [dir === -1 ? "right" : "left"]: 0,
              background: "var(--gradient-gold)",
            }}
          />
        </motion.div>
      ))}

      <Petals count={10} />

      <AnimatePresence>
        {!opening && (
          <motion.div
            className="relative z-10 flex flex-col items-center px-8 text-center"
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, filter: "blur(6px)" }}
            transition={{ duration: 0.9, ease: [0.22, 1, 0.36, 1] }}
          >
            <span className="text-gold/80 text-[0.55rem] tracking-[0.5em] uppercase">
              An engagement invitation
            </span>
            <h1 className="text-gold-foil font-display mt-5 text-5xl leading-none font-light">
              {wedding.bride.name}
              <span className="font-script text-gold/80 mx-3 text-3xl">&amp;</span>
              {wedding.groom.name}
            </h1>
            <span className="rule-gold mt-6 w-32" />

            <motion.button
              onClick={open}
              whileTap={{ scale: 0.92 }}
              whileHover={{ scale: 1.05 }}
              className="group relative mt-12 grid h-28 w-28 place-items-center"
              aria-label="Open the invitation"
            >
              <motion.span
                className="border-gold/40 absolute inset-0 rounded-full border"
                animate={{ scale: [1, 1.28, 1], opacity: [0.7, 0, 0.7] }}
                transition={{ repeat: Infinity, duration: 2.6, ease: "easeOut" }}
              />
              <motion.span
                className="shadow-gold grid h-20 w-20 place-items-center rounded-full"
                style={{ backgroundImage: "var(--gradient-gold)" }}
                animate={{ y: [0, -5, 0] }}
                transition={{ repeat: Infinity, duration: 3.4, ease: "easeInOut" }}
              >
                <span className="font-script text-emerald-ink text-3xl leading-none">
                  {wedding.bride.name[0]}
                  {wedding.groom.name[0]}
                </span>
              </motion.span>
            </motion.button>

            <motion.p
              className="text-ivory/60 mt-8 text-[0.6rem] tracking-[0.4em] uppercase"
              animate={{ opacity: [0.4, 1, 0.4] }}
              transition={{ repeat: Infinity, duration: 2.4 }}
            >
              Tap the seal to open
            </motion.p>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
