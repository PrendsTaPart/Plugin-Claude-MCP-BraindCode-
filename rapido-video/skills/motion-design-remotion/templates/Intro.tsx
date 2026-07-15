/** Gabarit INTRO (3-5 s) — logo + tagline, aux couleurs de la marque. */
import {AbsoluteFill, Img, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {brandSchema, SAFE, MIN, clampFont, ApercuWatermark} from './_shared';

export const introSchema = brandSchema.extend({
  tagline: z.string().default('Votre tagline ici'),
});

export const Intro: React.FC<z.infer<typeof introSchema>> = (b) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pop = spring({frame, fps, config: {damping: 200}});
  const logoScale = interpolate(pop, [0, 1], [0.7, 1]);
  const taglineY = interpolate(frame, [10, 30], [40, 0], {extrapolateRight: 'clamp'});
  const taglineOpacity = interpolate(frame, [10, 30], [0, 1], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{backgroundColor: b.secondary, fontFamily: b.fontFamily,
      justifyContent: 'center', alignItems: 'center', padding: SAFE.side}}>
      {b.logoUrl ? (
        <Img src={b.logoUrl} style={{width: 420, transform: `scale(${logoScale})`, opacity: pop}} />
      ) : (
        <div style={{width: 220, height: 220, borderRadius: 40, background: b.primary,
          transform: `scale(${logoScale})`, opacity: pop}} />
      )}
      <div style={{marginTop: 48, transform: `translateY(${taglineY}px)`, opacity: taglineOpacity,
        color: b.textColor, fontSize: clampFont(56, MIN.title), fontWeight: 800, textAlign: 'center'}}>
        {b.tagline}
      </div>
      <ApercuWatermark show={b.licence === 'apercu'} />
    </AbsoluteFill>
  );
};
