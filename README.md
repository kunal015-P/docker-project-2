# docker-project-2
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/docker-project-2.git
cd docker-project-2


# 2. Check Docker installation
docker --version
docker compose version


# 3. Build the Docker images
sudo docker compose build


# 4. Start the containers
sudo docker compose up -d


# 5. Verify running containers
sudo docker ps


# 6. Access PostgreSQL container
sudo docker exec -it docker-project-2-db-1 psql -U admin -d ecommerce


# 7. Create products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price INTEGER
);


# 8. Insert sample data
INSERT INTO products (name, price) VALUES ('Laptop', 800);
INSERT INTO products (name, price) VALUES ('Phone', 500);


# 9. Exit PostgreSQL
\q


# 10. Open application in browser
http://<EC2-PUBLIC-IP>:5000


# 11. Test products API
http://<EC2-PUBLIC-IP>:5000/products


# 12. View logs if needed
sudo docker compose logs


# 13. Stop containers
sudo docker compose down
