/** Gabarit STAT — barre de progression + compteur animé (stats, ex. PronoClip). */
import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {brandSchema, SAFE, MIN, clampFont, ApercuWatermark} from './_shared';

export const statBarSchema = brandSchema.extend({
  label: z.string().default('Taux de réussite'),
  valeur: z.number().default(87), // valeur finale (0-100)
  suffixe: z.string().default('%'),
});

export const StatBar: React.FC<z.infer<typeof statBarSchema>> = (b) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = interpolate(frame, [0, fps], [0, 1], {extrapolateRight: 'clamp'}); // ~1 s de montée
  const value = Math.round(t * b.valeur);
  const widthPct = t * Math.min(100, Math.max(0, b.valeur));

  return (
    <AbsoluteFill style={{backgroundColor: b.secondary, fontFamily: b.fontFamily,
      justifyContent: 'center', paddingLeft: SAFE.side, paddingRight: SAFE.side}}>
      <div style={{color: b.textColor, fontSize: clampFont(40, MIN.body), fontWeight: 700, marginBottom: 20}}>
        {b.label}
      </div>
      <div style={{height: 44, background: 'rgba(255,255,255,0.12)', borderRadius: 22, overflow: 'hidden'}}>
        <div style={{width: `${widthPct}%`, height: '100%', background: b.primary, borderRadius: 22}} />
      </div>
      <div style={{color: b.textColor, fontSize: clampFont(96, MIN.title), fontWeight: 900, marginTop: 24}}>
        {value}{b.suffixe}
      </div>
      <ApercuWatermark show={b.licence === 'apercu'} />
    </AbsoluteFill>
  );
};
