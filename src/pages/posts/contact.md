---
layout: '@/templates/BasePost.astro'
title: Contact
description: contactez moi dès maintenant !
pubDate: 2024-01-12T00:00:00Z
imgSrc: '/assets/images/icon-contact.png'
imgAlt: 'Avatar Elie'
---

# Contactez-moi

Pour me contacter, veuillez remplir le formulaire ci-dessous :

<form
  action="https://formspree.io/f/mvoegzkn"
  method="POST"
>
  <label for="nom" style="display: block; margin-bottom: 10px;">Nom :</label>
  <input type="text" id="nom" name="nom" required style="width: 100%; padding: 5px; margin-bottom: 10px; border-radius: 5px; color: black;">

  <label for="nom" style="display: block; margin-bottom: 10px;">Prénom :</label>
  <input type="text" id="nom" name="nom" required style="width: 100%; padding: 5px; margin-bottom: 10px; border-radius: 5px; color: black;">

  <label for="email" style="display: block; margin-bottom: 10px;">Email :</label>
  <input type="email" id="email" name="email" required style="width: 100%; padding: 5px; margin-bottom: 10px; border-radius: 5px; color: black;">

  <label for="message" style="display: block; margin-bottom: 10px;">Message :</label>
  <textarea id="message" name="message" required style="width: 100%; padding: 5px; margin-bottom: 10px; border-radius: 5px; color: black;"></textarea>

  <button type="submit" style="background-color: #007bff; color: #fff; padding: 10px 20px; border: none; border-radius: 5px;">Envoyer</button>
</form>

