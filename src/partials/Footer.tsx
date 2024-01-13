import { Section } from 'astro-boilerplate-components';

const Footer = () => (
  <Section>
    <footer>
      <div style={{ textAlign: 'center' }}>
        <p>
          <a
            className="text-cyan-400 hover:underline"
            href="mailto:elie.garcia85670@gmail.com"
          >
            Envoyer un e-mail: elie.garcia85670@gmail.com
          </a>
        </p>
        <p>
          <a className="text-cyan-400 hover:underline" href="tel:0774890309">
            Telephone: 07 74 89 03 09{' '}
          </a>
        </p>
      </div>
    </footer>
  </Section>
);

export { Footer };
