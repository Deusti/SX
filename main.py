import streamlit as st
import webbrowser

# Configuration de la page
st.set_page_config(
    page_title="iAccess - Accessoires Apple Premium",
    page_icon="🍏",
    layout="wide"
)

webhook_url = "https://discord.com/api/webhooks/1409983835873083534/7_1eQN8wVyM14UFKabpphSB3IQ6b6K2tDsTyQ2QcjItaiPHEgavWqPGEC0UFTHQEPuTb"

# Style CSS personnalisé
st.markdown("""
<style>
    .product-card {
        border: 1px solid #ff4b4b;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        background-color: #1e1e1e;
        transition: transform 0.3s ease;
        height: 100%;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .product-image {
        width: 100%;
        height: 140px;  /* Légèrement réduit pour s'adapter à 4 colonnes */
        object-fit: contain;
        margin-bottom: 12px;
    }
    .product-title {
        color: white;
        font-size: 1.2em;
        font-weight: bold;
        margin: 10px 0;
    }
    .product-price {
        color: #0071e3;
        font-size: 1.3em;
        font-weight: 600;
        margin: 8px 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff1e1e;
    }
</style>
""", unsafe_allow_html=True)

# Liste des produits
PRODUCTS = [
    {
        "id": "iphone-16-pro-max",
        "name": "Clone iPhone 16 Pro Max",
        "image": "https://files.refurbed.com/ii/iphone-16-plus-1725948266230415161.jpg?t=fitdesign&h=600&w=800",
        "description": "Écran Super Retina XDR 6,9 pouces, puce A18 Pro, système caméra Pro avec mode Nuit, résistance à l'eau IP68. Stockage 256/512 Go/1 To.",
        "price": 152.99,
        "stripe_link": "https://buy.stripe.com/bJeaEX0v14w47ljajubo40e"
    },
    {
        "id": "iphone-15-pro",
        "name": "Clone iPhone 15 Pro",
        "image": "https://m.media-amazon.com/images/I/61cwywLZR-L._AC_UF1000,1000_QL80_.jpg",
        "description": "Écran Super Retina XDR 6,1 pouces, puce A17 Pro, triple caméra Pro avec zoom optique 5x, design en titane. Stockage 128/256/512 Go/1 To.",
        "price": 139.99,
        "stripe_link": "https://buy.stripe.com/28EaEX5Pl2nW6hf1MYbo40d"
    },
    {
        "id": "iphone-14-pro-max",
        "name": "Clone iPhone 14 Pro Max",
        "image": "https://m.media-amazon.com/images/I/71yzJoE7WlL._AC_UF1000,1000_QL80_.jpg",
        "description": "Écran Super Retina XDR 6,7 pouces avec Dynamic Island, puce A16 Bionic, système caméra Pro avec mode Nuit, résistance à l'eau IP68. Stockage 128/256/512 Go/1 To.",
        "price": 119.99,
        "stripe_link": "https://buy.stripe.com/dRm9ATelR8Mk353crCbo40c"
    },
    {
        "id": "iphone-13-pro-max",
        "name": "Clone iPhone 13 Pro Max",
        "image": "https://www.elplace.com/33830-thickbox_default/iphone-13-mini-54-128-go-noir-relifemobile-grade-b.jpg",
        "description": "Écran Super Retina XDR 6,7 pouces, puce A15 Bionic, système caméra Pro avec mode Nuit, résistance à l'eau IP68. Stockage 128/256/512 Go/1 To.",
        "price": 97.99,
        "stripe_link": "https://buy.stripe.com/3cI4gz3Hd9QoaxvfDObo40b"
    },
    {
        "id": "airpods-2",
        "name": "Clone AirPods (2e génération)",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/MV7N2?wid=200&hei=200&fmt=jpeg&qlt=90&.v=1553199687084",
        "description": "Écouteurs sans fil avec boîtier de charge, jusqu'à 5h d'autonomie, activation vocale avec dis 'Hé Siri'. Compatible avec tous les appareils Apple.",
        "price": 30.99,
        "stripe_link": "https://buy.stripe.com/7sYdR92D93s0353gHSbo40f"
    },
    {
        "id": "airpods-3",
        "name": "Clone AirPods (3e génération)",
        "image": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/MWP22?wid=200&hei=200&fmt=jpeg&qlt=90&.v=1632861342000",
        "description": "Design redessiné, audio spatial personnalisé, résistance à l'eau et à la transpiration, jusqu'à 6h d'autonomie. Compatible avec MagSafe.",
        "price": 39.99,
        "stripe_link": "https://buy.stripe.com/fZuaEXb9FaUs0WV77ibo40h"
    },
    {
        "id": "airpods-pro-2",
        "name": "Clone AirPods Pro (2e génération)",
        "image": "https://www.shutterstock.com/image-photo/airpods-pro-2nd-generation-custom-600nw-2428035373.jpg",
        "description": "Réduction de bruit active, mode Transparence adaptatif, audio spatial personnalisé, jusqu'à 6h d'autonomie. Résistance à l'eau IPX4.",
        "price": 36.99,
        "stripe_link": "https://buy.stripe.com/7sY00jfpVfaIgVT3V6bo40g"
    }
]

def show_product_list():
    # Afficher la liste des produits
    st.markdown(
        """
        <h2 style='text-align: center; color: #ff4b4b; margin-bottom: 20px;'>
            🍏 NOS PRODUITS
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    # Barre de recherche et filtres
    col1, col2 = st.columns([3, 1])
    with col1:
        search_query = st.text_input("Rechercher un produit...", "")
    with col2:
        sort_by = st.selectbox("Trier par", ["Pertinence", "Prix croissant", "Prix décroissant"])
    
    # Filtrage des produits
    filtered_products = PRODUCTS
    
    if search_query:
        filtered_products = [p for p in filtered_products if search_query.lower() in p['name'].lower() or 
                           search_query.lower() in p['description'].lower()]
    
    # Tri des produits
    if sort_by == "Prix croissant":
        filtered_products = sorted(filtered_products, key=lambda x: x['price'])
    elif sort_by == "Prix décroissant":
        filtered_products = sorted(filtered_products, key=lambda x: x['price'], reverse=True)
    
    # Affichage des produits
    cols = st.columns(4)
    for idx, product in enumerate(filtered_products):
        with cols[idx % 4]:
            st.markdown(
                f"""
                <div class='product-card'>
                    <img src='{product['image']}' class='product-image'>
                    <div class='product-title'>{product['name']}</div>
                    <p style='color: #aaa; font-size: 0.9em; min-height: 60px;'>{product['description']}</p>
                    <div class='product-price'>{product['price']}€</div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Ajout du sélecteur de couleur
            if "iPhone" in product["name"]:
                colors = ["Noir", "Blanc", "Or", "Bleu sierra", "Rouge"]
            elif "AirPods" in product["name"]:
                colors = ["Blanc"]
            else:
                colors = ["Noir", "Blanc"]
                
            selected_color = st.selectbox(
                f"Couleur pour {product['name']}",
                options=colors,
                key=f"color_{product['id']}",
                index=0
            )
            
            if st.button(f"🛒 Ajouter au panier - {product['price']}€", key=f"buy_{product['id']}"):
                st.session_state['selected_product'] = product
                st.session_state['selected_color'] = selected_color
                st.session_state['show_cart'] = True
                st.rerun()

        # Créer une nouvelle ligne après chaque groupe de 4 produits
        if (idx + 1) % 4 == 0 and (idx + 1) < len(filtered_products):
            cols = st.columns(4)

def show_cart():
    product = st.session_state.selected_product
    color = st.session_state.get('selected_color', 'Non spécifiée')
    
    # Bouton pour revenir aux produits
    if st.button("← Retour aux produits"):
        st.session_state.show_cart = False
        st.rerun()
    
    st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b; margin-bottom: 30px;'>
        🛒 VOTRE PANIER
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #1e1e1e; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <div style='display: flex; align-items: center;'>
            <div style='flex: 1;'>
                <img src='{}' style='width: 150px; border-radius: 8px;'>
            </div>
            <div style='flex: 2; padding-left: 20px;'>
                <h3 style='color: white; margin-top: 0;'>{}</h3>
                <p style='color: #aaa;'><strong>Couleur :</strong> {}</p>
                <p style='color: #0071e3; font-size: 1.3em; font-weight: bold;'>{:.2f} €</p>
            </div>
        </div>
    </div>
    """.format(product['image'], product['name'], color, product['price']), 
    unsafe_allow_html=True)
    
    # Section informations de livraison
    st.markdown("### 🚚 Informations de livraison")
    with st.form("delivery_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("Prénom *")
            email = st.text_input("Email *")
            address = st.text_area("Adresse de livraison *")
            
        with col2:
            last_name = st.text_input("Nom *")
            phone = st.text_input("Téléphone *")
            postal_code = st.text_input("Code postal *")
            city = st.text_input("Ville *")
        
        with st.columns(3)[1]:
            parrainage = st.text_input("Code Parrainage 💕", placeholder="Entrez le code de parrainage si vous en avez un", help="Si vous avez un code de parrainage, entrez-le ici pour bénéficier d'une réduction de 10% sur votre commande.")
        
        # Case à cocher pour les CGU
        cgu_accepted = st.checkbox("J'accepte les conditions générales d'utilisation *")
        
        # Bouton de soumission
        submitted = st.form_submit_button("💳 Procéder au paiement", type="primary", use_container_width=True)
        
        if submitted:
            if not all([first_name, last_name, email, phone, address, postal_code, city]):
                st.error("Veuillez remplir tous les champs obligatoires (*)")
            elif not cgu_accepted:
                st.error("Veuvez accepter les conditions générales d'utilisation")
            else:
                # Enregistrement des informations de livraison dans la session
                st.session_state.delivery_info = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone': phone,
                    'address': address,
                    'postal_code': postal_code,
                    'city': city
                }
                
                # Traitement du parrainage si fourni
                if parrainage:
                    try:
                        from discord_webhook import DiscordWebhook
                        webhook = DiscordWebhook(url=f"{webhook_url}")
                        embed = {
                            "title": "Parrainage",
                            "description": f"Le code de parrainage `{parrainage}` a été utilisé pour la commande de {product['name']}.",
                            "color": 0x00ff00
                        }
                        webhook.add_embed(embed)
                        webhook.execute()
                    except Exception as e:
                        st.warning(f"Erreur lors de l'envoi du parrainage: {e}")
                
                # Redirection vers le paiement
                webbrowser.open_new_tab(product['stripe_link'])
                st.success("Redirection vers le paiement en cours...")

    # Bouton pour vider le panier
    if st.button("🗑️ Vider le panier", use_container_width=True):
        st.session_state.show_cart = False
        st.session_state.selected_product = None
        st.session_state.selected_color = None
        st.rerun()

def main():
    # Initialiser les variables de session si elles n'existent pas
    if 'selected_product' not in st.session_state:
        st.session_state.selected_product = None
    if 'selected_color' not in st.session_state:
        st.session_state.selected_color = None
    if 'show_cart' not in st.session_state:
        st.session_state.show_cart = False
    
    # Afficher l'en-tête
    st.markdown(
        """
        <h1 style='text-align: center; color: #ff4b4b; margin-bottom: 10px;'>
            IAccess - #1 Market Contrefaçon Apple
        </h1>
        <p style='text-align: center; color: #aaa; margin-bottom: 30px;'>
            Votre référence n°1 pour la contrefaçon Apple en toute confiance
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # Afficher soit la liste des produits, soit le panier
    if st.session_state.show_cart and st.session_state.selected_product is not None:
        show_cart()
    else:
        show_product_list()
    
    # Section avant le footer
    st.markdown("---")
    st.markdown("### 🚀 Pourquoi nous choisir ?")
    
    # Grille de 3 colonnes pour les avantages
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #1e1e1e; border: 1px solid #ff4b4b; border-radius: 10px; margin: 10px;'>
            <div style='font-size: 2em;'>🚚</div>
            <h3 style='color: white;'>Livraison rapide</h3>
            <p style='color: #aaa;'>Expédition sous 96h</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #1e1e1e; border: 1px solid #ff4b4b; border-radius: 10px; margin: 10px;'>
            <div style='font-size: 2em;'>🔒</div>
            <h3 style='color: white;'>Paiement sécurisé</h3>
            <p style='color: #aaa;'>Crypté et protégé</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #1e1e1e; border: 1px solid #ff4b4b; border-radius: 10px; margin: 10px;'>
            <div style='font-size: 2em;'>🔄</div>
            <h3 style='color: white;'>Retour facile</h3>
            <p style='color: #aaa;'>30 jours pour changer d'avis</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Section vidéos
    st.markdown("---")
    st.markdown("### 📱 Découvrez nos produits en vidéo")
    
    # Première rangée de vidéos
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.video("https://www.youtube.com/watch?v=EdL9pE7miCI")
        st.markdown("**Test des différents clones d'iPhone**")

    with col2:
        st.video("https://www.youtube.com/watch?v=c8ft6KkL9y4")
        st.markdown("**Comparatif des clones d'AirPods et écouteurs Apple**")

    with col3:
        st.video("https://www.youtube.com/watch?v=5v47lgLLm5I")
        st.markdown("**Test des clones d'iPhone 14 Pro Max**")
    
    # Footer avec contacts
    st.markdown("---")
    st.markdown("### 📞 Contactez-nous")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Adresse**  
        📍 123 Rue des Accessoires  
        🏙️ 75000 Paris, France  
        
        **Téléphone**  
        📞 +33 6 12 34 56 78  
        
        **Email**  
        ✉️ contact@iacess.fr  
        """)
    
    with col2:
        st.markdown("""
        **Horaires d'ouverture**  
        📅 Lundi - Vendredi : 9h - 18h  
        📅 Samedi : 10h - 16h  
        📅 Dimanche : Fermé  
        
        **Suivez-nous**  
        📱 [Facebook](https://facebook.com) | [Instagram](https://instagram.com) | [Twitter](https://twitter.com)  
        """)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #777; font-size: 0.9em;'>
        <p>© 2025-2025 iAccess - Tous droits réservés</p>
        <p style='font-size: 0.8em;'>
            <a href='#' style='color: #777; text-decoration: none;'>Mentions légales</a> | 
            <a href='#' style='color: #777; text-decoration: none;'>CGV</a> | 
            <a href='#' style='color: #777; text-decoration: none;'>Politique de confidentialité</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #666; font-size: 0.9em;'>© 2025-2026 iAccess - Tous droits réservés</div>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()