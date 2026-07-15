/**
 * Socle partagé des gabarits de marque (Remotion).
 * Paramétrage par la charte : couleurs hex, police mappée, logo depuis l'URL CMS.
 * Règles de rendu encodées : safe zones + tailles de police minimales.
 */
import {z} from 'zod';

// Schéma de marque — alimenté depuis get_brand / ./rapido-kb/charte-graphique.md.
export const brandSchema = z.object({
  primary: z.string().default('#0052FF'), // couleur principale (hex)
  secondary: z.string().default('#111111'),
  textColor: z.string().default('#FFFFFF'),
  fontFamily: z.string().default('Inter, system-ui, sans-serif'), // police mappée
  logoUrl: z.string().default(''), // URL publique CMS (list_all_files/get_brand)
  // Mode licence : 'apercu' (défaut, non commercial) tant que la décision Remotion
  // n'est pas tranchée en V0 ; 'commercial' une fois la licence validée.
  licence: z.enum(['apercu', 'commercial']).default('apercu'),
});
export type Brand = z.infer<typeof brandSchema>;

// Safe zones (px, base 1080x1920) et tailles de police minimales.
export const SAFE = {top: 150, bottom: 170, side: 60};
export const MIN = {title: 56, body: 36, floor: 28};
export const clampFont = (v: number, floor = MIN.floor) => Math.max(v, floor);

// Bandeau « APERÇU » quand la licence n'est pas tranchée (usage non commercial).
export const ApercuWatermark: React.FC<{show: boolean}> = ({show}) =>
  show ? (
    <div style={{
      position: 'absolute', top: SAFE.top / 2, right: SAFE.side,
      padding: '8px 16px', borderRadius: 8, background: 'rgba(0,0,0,0.55)',
      color: '#FFD400', fontSize: clampFont(28), fontWeight: 700,
      letterSpacing: 1,
    }}>APERÇU — licence Remotion non tranchée · usage non commercial</div>
  ) : null;
