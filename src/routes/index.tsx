import { createFileRoute } from "@tanstack/react-router";
import { AnimatePresence, motion } from "framer-motion";
import { useEffect, useState } from "react";
import { Hero } from "@/components/wedding/Hero";
import { Couple } from "@/components/wedding/Couple";
import { Countdown } from "@/components/wedding/Countdown";
import { EventDetails } from "@/components/wedding/EventDetails";
import { Footer } from "@/components/wedding/Footer";
import { MusicPlayer } from "@/components/wedding/MusicPlayer";
import { Opener } from "@/components/wedding/Opener";
import { ScrollProgress } from "@/components/wedding/ScrollProgress";

const title = "Koushik & Ranjitha — Engagement Invitation · 21 September 2026";
const description =
  "Celebrate the engagement of Koushik & Ranjitha on Monday, 21 September 2026 in Shivamogga, Karnataka.";
const url = "https://ranjitha-weds-koushika.invitingyou.top";
const image = "https://ranjitha-weds-koushika.invitingyou.top/og-image.jpg";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title },
      { name: "description", content: description },
      { property: "og:site_name", content: "Koushik & Ranjitha" },
      { property: "og:title", content: title },
      { property: "og:description", content: description },
      { property: "og:type", content: "website" },
      { property: "og:url", content: url },
      { property: "og:image", content: image },
      { property: "og:image:type", content: "image/jpeg" },
      { property: "og:image:width", content: "1200" },
      { property: "og:image:height", content: "630" },
      {
        property: "og:image:alt",
        content: "Portrait of Koushik & Ranjitha — Engagement Invitation",
      },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:url", content: url },
      { name: "twitter:title", content: title },
      { name: "twitter:description", content: description },
      { name: "twitter:image", content: image },
    ],
    links: [{ rel: "canonical", href: url }],
  }),
  component: Invitation,
});

function Invitation() {
  const [opened, setOpened] = useState(false);
  const [musicTrigger, setMusicTrigger] = useState(false);

  useEffect(() => {
    document.body.style.overflow = opened ? "" : "hidden";
    return () => {
      document.body.style.overflow = "";
    };
  }, [opened]);

  return (
    <>
      <AnimatePresence>
        {!opened && (
          <Opener
            key="opener"
            onStartOpen={() => setMusicTrigger(true)}
            onOpen={() => setOpened(true)}
          />
        )}
      </AnimatePresence>

      <MusicPlayer autoPlayTrigger={musicTrigger || opened} />

      {opened && <ScrollProgress />}

      <motion.main
        initial={{ opacity: 0, scale: 1.03 }}
        animate={opened ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 1.03 }}
        transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
        className="bg-background mx-auto w-full max-w-[520px] overflow-hidden"
      >
        <Hero />
        <Couple />
        <Countdown />
        <EventDetails />
        <Footer />
      </motion.main>
    </>
  );
}
