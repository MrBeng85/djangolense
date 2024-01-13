import {
  GradientText,
  HeroAvatar,
  HeroSocial,
  Section,
} from 'astro-boilerplate-components';

const Hero = () => (
  <Section>
    <HeroAvatar
      title={
        <>
          Salut moi c'est <GradientText>Elie</GradientText> 👋
        </>
      }
      description={
        <>
          Je suis developpeur Python spécialisé sur le framework{' '}
          <a
            className="text-cyan-400 hover:underline"
            href="https://python.doctor/page-django-introduction-python/"
          >
            Django
          </a>{' '}
          Je suis capable de créer de A a Z un site web dynamique pour tout vos{' '}
          <a
            className="text-cyan-400 hover:underline"
            href="https://www.youtube.com/watch?v=sF_I5HETAfQ&ab_channel=Graven-D%C3%A9veloppement/"
          >
            besoins
          </a>{' '}
          n'hésitez pas a me contacter, me suivre sur les réseaux sociaux ou
          aller faire un tour sur ma page{' '}
          <a className="text-cyan-400 hover:underline" href="/posts/about/">
            About
          </a>{' '}
          pour en savoir plus sur moi
        </>
      }
      avatar={
        <img
          className="h-80 w-80"
          src="/assets/images/AvatarMaker.png"
          alt="Avatar image"
          loading="lazy"
        />
      }
      socialButtons={
        <>
          <a href="https://www.linkedin.com/in/elie-garcia-978b0928a/">
            <HeroSocial
              src="/assets/images/linkedin-icon.png"
              alt="Linkedin icon"
            />
          </a>
          <a href="tel:0774890309">
            <HeroSocial
              src="/assets/images/icon-telephone.png"
              alt="Tel icon"
            />
          </a>
          <a href="mailto:elie.garcia85670@gmail.com">
            <HeroSocial src="/assets/images/icon-mail.png" alt="Mail icon" />
          </a>
        </>
      }
    />
  </Section>
);

export { Hero };
