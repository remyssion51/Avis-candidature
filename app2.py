import streamlit as st
import datetime

# --- Configuration de la page ---
st.set_page_config(page_title="Feedback Recruteur", page_icon="💼", layout="centered")

# --- Navigation entre deux pages ---
page = st.sidebar.radio("Navigation", ["Laisser un commentaire", "Espace privé (admin)"])

# --- PAGE 1 : Formulaire de feedback ---
if page == "Laisser un commentaire":
    st.title("💬 Laissez un commentaire sur la candidature")
    st.write("Merci de prendre un moment pour partager votre avis sur la candidature de [Ton Nom].")

    with st.form("feedback_form"):
        nom = st.text_input("👤 Votre nom ou fonction (optionnel)")
        entreprise = st.text_input("🏢 Nom de l’entreprise (optionnel)")
        note = st.slider("⭐ Évaluation de la candidature", 1, 5, 3)
        commentaire = st.text_area("📝 Votre commentaire", placeholder="Exemple : Le profil correspond bien au poste...")
        date = datetime.date.today()

        submit = st.form_submit_button("Envoyer le commentaire")

        if submit:
            if commentaire.strip() == "":
                st.error("Veuillez écrire un commentaire avant d’envoyer.")
            else:
                with open("feedback_recruteurs.txt", "a", encoding="utf-8") as f:
                    f.write(f"{date} | {nom} | {entreprise} | Note: {note}/5 | {commentaire}\n")
                st.success("✅ Merci ! Votre commentaire a été enregistré avec succès.")
                st.balloons()

# --- PAGE 2 : Accès privé ---
elif page == "Espace privé (admin)":
    st.title("🔒 Espace privé du candidat")

    mdp = st.text_input("Mot de passe", type="password")

    if mdp == "remsrems78":  # 👉 à personnaliser
        st.success("Accès autorisé ✅")
        st.subheader("📂 Commentaires reçus")

        try:
            with open("feedback_recruteurs.txt", "r", encoding="utf-8") as f:
                lignes = f.readlines()
                if lignes:
                    for ligne in reversed(lignes):
                        date, nom, entreprise, note, commentaire = ligne.split(" | ", 4)
                        st.markdown(f"**🗓️ {date.strip()}** — {nom.strip()} ({entreprise.strip()})")
                        st.markdown(f"⭐ **{note.strip()}**")
                        st.markdown(f"💬 {commentaire.strip()}")
                        st.markdown("---")
                else:
                    st.info("Aucun commentaire pour le moment.")
        except FileNotFoundError:
            st.info("Aucun commentaire enregistré.")
    elif mdp:
        st.error("Mot de passe incorrect.")
